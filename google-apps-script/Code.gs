/**
 * Invest 4U Solutions: website form → email (Google Apps Script web app)
 *
 * Handles both forms on invest4u.in:
 *   - Contact form (home page + contact.html): name, phone, email, service, preferred_time, message, consent
 *   - Free Financial Checkup (financial-checkup.html): name, age_group, goals[], existing_cover, phone, email, consent
 * main.js also sends: subject, form, page, page_title.
 *
 * Setup:
 *   1. script.google.com → New project → paste this file → Save.
 *   2. Deploy → New deployment → type "Web app"
 *        Execute as: Me    Who has access: Anyone
 *   3. Approve the permissions (sending email as you).
 *   4. Copy the /exec URL into FORM_ENDPOINT at the top of invest4u/js/main.js.
 *   After editing this script: Deploy → Manage deployments → Edit → Version: New version (the URL stays the same).
 *
 * Quota: a free Gmail account can send about 100 emails a day with MailApp (Workspace: 1,500).
 */

var RECIPIENT_EMAIL = "info@invest4u.in"; // where enquiries land (comma-separate to add more)
var SENDER_NAME = "Invest 4U Website";
var TIMEZONE = "Asia/Kolkata";

// Fields shown in the email, in this order. Anything else that arrives is listed after them.
var FIELDS = [
  ["name", "Name"],
  ["phone", "Phone"],
  ["email", "Email"],
  ["service", "Service interested in"],
  ["preferred_time", "Preferred call time"],
  ["age_group", "Age group"],
  ["goals[]", "Goals"],
  ["existing_cover", "Existing insurance cover"],
  ["message", "Message"],
  ["consent", "Consent to be contacted"],
];
// Sent by the page but not worth listing in the email
var SKIP = ["subject", "form", "page", "page_title", "botcheck", "access_key", "from_name"];

function doPost(e) {
  try {
    var params = (e && e.parameters) || {}; // every value is an array (goals[] can have several)

    // Honeypot ticked: a bot. Report success and send nothing.
    if (get(params, "botcheck")) return jsonOutput({ result: "success" });

    var name = get(params, "name");
    var phone = get(params, "phone");
    var email = get(params, "email");
    if (!name || !phone) {
      return jsonOutput({ result: "error", message: "Name and phone are required." });
    }

    var formType = get(params, "form") || "Website enquiry";
    var subject = (get(params, "subject") || "New enquiry from invest4u.in") + ": " + name;
    var service = get(params, "service");
    if (service) subject += " (" + service + ")";

    // Collect the rows to show: known fields first, then any extras
    var rows = [];
    FIELDS.forEach(function (f) {
      var v = get(params, f[0]);
      if (v) rows.push([f[1], v]);
    });
    Object.keys(params).forEach(function (key) {
      var known = FIELDS.some(function (f) { return f[0] === key; });
      if (!known && SKIP.indexOf(key) === -1) {
        var v = get(params, key);
        if (v) rows.push([prettyLabel(key), v]);
      }
    });

    var submitted = Utilities.formatDate(new Date(), TIMEZONE, "dd MMM yyyy, hh:mm a");
    var page = get(params, "page") || "(unknown page)";
    var pageTitle = get(params, "page_title");

    var body =
      formType + " from the Invest 4U website\n\n" +
      rows.map(function (r) {
        return r[0] + ": " + (r[1].indexOf("\n") > -1 ? "\n" + r[1] : r[1]);
      }).join("\n") +
      "\n\nSubmitted: " + submitted + " IST" +
      "\nPage: " + (pageTitle ? pageTitle + " – " : "") + page;

    var htmlBody =
      '<div style="font-family:Arial,sans-serif;font-size:14px;color:#1e293b;max-width:600px">' +
      '<h2 style="margin:0 0 16px;color:#013364;font-size:18px">' + esc(formType) + "</h2>" +
      '<table cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%">' +
      rows.map(function (r) {
        return '<tr><td style="border-bottom:1px solid #e2e8f0;width:38%;color:#475569;vertical-align:top"><b>' +
          esc(r[0]) + '</b></td><td style="border-bottom:1px solid #e2e8f0;white-space:pre-wrap">' +
          linkify(r[0], r[1]) + "</td></tr>";
      }).join("") +
      "</table>" +
      '<p style="margin:16px 0 0;font-size:12px;color:#64748b">Submitted ' + esc(submitted) + " IST from " +
      '<a href="' + esc(page) + '">' + esc(pageTitle || page) + "</a></p></div>";

    var options = { name: SENDER_NAME, htmlBody: htmlBody };
    if (isValidEmail(email)) options.replyTo = email; // "Reply" goes straight to the client

    MailApp.sendEmail(RECIPIENT_EMAIL, subject, body, options);
    return jsonOutput({ result: "success" });
  } catch (err) {
    console.error(err);
    return jsonOutput({ result: "error", message: String(err) });
  }
}

// Open the /exec URL in a browser to check the deployment is live.
function doGet() {
  return jsonOutput({ status: "ok", message: "Invest 4U form endpoint is live." });
}

// Run this once from the editor to test sending (and to grant the email permission).
function testSend() {
  doPost({
    parameters: {
      form: ["Contact form"],
      subject: ["New enquiry from invest4u.in"],
      name: ["Test User"],
      phone: ["+91 98765 43210"],
      email: ["test@example.com"],
      service: ["Life Insurance"],
      preferred_time: ["Morning (9 AM to 12 PM)"],
      message: ["This is a test message."],
      consent: ["yes"],
      page: ["https://www.invest4u.in/contact.html"],
    },
  });
}

/* ---------- helpers ---------- */

// Joined, trimmed value of a field ("" if missing)
function get(params, key) {
  var v = params[key];
  if (v === undefined) return "";
  return (Array.isArray(v) ? v : [v])
    .map(function (x) { return String(x).trim(); })
    .filter(String)
    .join(", ");
}

function prettyLabel(key) {
  var s = key.replace(/\[\]$/, "").replace(/[_-]+/g, " ");
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function linkify(label, value) {
  if (label === "Email" && isValidEmail(value)) return '<a href="mailto:' + esc(value) + '">' + esc(value) + "</a>";
  if (label === "Phone") {
    var digits = value.replace(/[^\d+]/g, "");
    var wa = digits.replace(/^\+/, "");
    if (wa.length === 10) wa = "91" + wa;
    return '<a href="tel:' + esc(digits) + '">' + esc(value) + '</a> · <a href="https://wa.me/' + esc(wa) + '">WhatsApp</a>';
  }
  if (label === "Consent to be contacted") return /^(on|yes)$/i.test(value) ? "Yes" : esc(value);
  return esc(value);
}

function esc(s) {
  return String(s)
    .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function jsonOutput(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

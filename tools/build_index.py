from build import *
from pages_common import partner_grid
from pages_blog import featured_articles
SRC = TOOLS + 'src/'

ORG = {
    "@context": "https://schema.org",
    "@type": "FinancialService",
    "@id": "https://www.invest4u.in/#organization",
    "name": "Invest 4U Solutions",
    "legalName": "K & VK Invest 4U Advisory Services LLP",
    "slogan": "Financial Architects",
    "description": "Insurance and investment advisory firm in Kochi, Kerala, serving families and businesses since 1992.",
    "url": "https://www.invest4u.in/",
    "logo": "https://www.invest4u.in/assets/images/logo.png",
    "image": "https://www.invest4u.in/assets/images/og-image.jpg",
    "foundingDate": "1992",
    "founder": {"@type": "Person", "name": "K.N. Krishnankutty", "jobTitle": "Founder & Managing Director"},
    "telephone": "+91-98470-46614",
    "email": "info@invest4u.in",
    "priceRange": "Free consultation",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Vaikkom Road, Kannankulangara",
        "addressLocality": "Tripunithura, Kochi",
        "addressRegion": "Kerala",
        "postalCode": "682301",
        "addressCountry": "IN"
    },
    "geo": {"@type": "GeoCoordinates", "latitude": 9.9447, "longitude": 76.3445},
    "hasMap": "https://www.google.com/maps?q=Kannankulangara,+Tripunithura,+Kochi,+Kerala+682301",
    "openingHoursSpecification": [{
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "09:00",
        "closes": "18:30"
    }],
    "areaServed": {"@type": "City", "name": "Kochi"},
    "department": [{
        "@type": "FinancialService",
        "name": "Invest 4U Solutions, Infopark Branch",
        "telephone": "+91-98470-56614",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Ground Floor, Thapasya Building, Infopark",
            "addressLocality": "Kakkanad, Kochi",
            "addressRegion": "Kerala",
            "addressCountry": "IN"
        }
    }],
    "sameAs": [
        "https://www.facebook.com/investmests4u/",
        "https://in.linkedin.com/company/invest4usolutions",
        "https://www.instagram.com/invest4u.in/",
        "https://wa.me/919847046614"
    ]
}

def main():
    preload = ('<link rel="preload" as="image" href="assets/videos/hero-1-mobile.webp" media="(max-width: 767px)" fetchpriority="high">\n'
               '<link rel="preload" as="image" href="assets/videos/hero-1.webp" media="(min-width: 768px)" fetchpriority="high">')
    build('index.html',
          title='Home',
          full_title='Invest 4U Solutions | Insurance & Investment Advisors, Kochi',
          desc='Invest 4U Solutions, Financial Architects since 1992: life, health and corporate insurance, mutual funds, retirement and tax planning in Kochi, Kerala.',
          main=open(SRC + 'index-main.html').read().replace('{{partners}}', partner_grid()).replace('{{blog}}', featured_articles()),
          current='index.html',
          loader=True,
          preload=preload,
          extra_head=SWIPER_CSS + '\n' + AOS_CSS,
          extra_scripts=SWIPER_JS + '\n' + AOS_JS,
          jsonld=ORG)


if __name__ == '__main__':
    main()

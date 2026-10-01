from build import *
SRC = TOOLS + 'src/'

def main():
    build('styleguide.html',
          title='Style Guide',
          desc='Internal style guide for the Invest 4U Solutions website.',
          main=open(SRC + 'styleguide-main.html').read(),
          robots='noindex, nofollow')


if __name__ == '__main__':
    main()

import '@/styles/globals.css'
import { Manrope } from 'next/font/google'
import { AppPropsWithLayout } from '@/typescript/nextpage'

const manrope = Manrope({
  subsets: ['latin'],
});

function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  // get layout
  const getLayout = Component.getLayout || ((page) => page);
  return getLayout(
    <>
      <style jsx global>
        {`
          :root {
            --manrope-font: ${manrope.style.fontFamily};
          }
        `}
      </style>
      <Component {...pageProps} />
    </>
  );
}
export default MyApp;
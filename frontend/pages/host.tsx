import Layout from '@/components/layouts/mobile'
import { toast } from 'react-toastify'
import { themesMap } from '@/shared/constants'
import { GetServerSideProps } from 'next'
import QRCode from 'react-qr-code'
import { Notepad, SpotifyLogo, X } from 'phosphor-react'

const handleToast = () => {
  toast('Loading...', {
    // toastId: "123",
    position: "bottom-center",
    autoClose: 3000,
    style: { marginTop: "20px",  marginBottom: "0px" },
  });
};

export default function HostSession({ themeID }: { themeID: string }) {
  return (
    <div className="flex flex-col justify-between h-full w-full">
      <div>
        <p className="text-xl font-semibold">
          Session is Active
        </p>
        <p className="text-sm text-gray-600 mt-1">
          Theme: <span className="text-blue-600 font-semibold">{themesMap.get(themeID)}</span>
        </p>

        <hr className="mt-5 mb-4" />

        <div>
          <div className="flex items-center gap-x-2">
            <Notepad size={28} />
            <span className="text-base text-gray-800">Instructions</span>
          </div>

          <p className="text-sm text-gray-600 mt-2">1. Use the QR Code to let people join your session.</p>
        </div>

        <div className="px-6 mt-7">
          <QRCode
            size={256}
            style={{ height: "auto", maxWidth: "100%", width: "100%" }}
            value={`https://www.musix.vercel.app/join/${themeID}`}
            viewBox={`0 0 256 256`}
          />
        </div>

        <div className="mt-6">
          <p className="text-sm text-gray-600">
            2. Open the
            <span className="text-[#1db954] w-min mx-1"><SpotifyLogo size={32} color="#1db954" className="inline mb-1" /> Spotify</span>
            app on your phone and start playing music!
          </p>

          <p className="text-sm text-gray-600 mt-2">3. New songs will be queued every minute.</p>
        </div>
      </div>

      <button className="flex items-center justify-center gap-x-2 py-3 rounded-full mt-8 bg-blue-500">
        <X size={24} color="#fff" weight='fill' />
        <p className="text-white font-semibold">
          Stop Session
        </p>
      </button>
    </div>
  )
}

export const getServerSideProps: GetServerSideProps<{ themeID: string }> = async (context) => {
  // get query params
  const { theme } = context.query;
  return {
    props: {
      themeID: theme as string,
    },
  };
}

HostSession.getLayout = function getLayout(page: React.ReactElement) {
  return <Layout>{page}</Layout>;
}
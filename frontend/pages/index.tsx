import { Waveform } from '@uiball/loaders'
import { SpotifyLogo } from 'phosphor-react'
import useMusixStore from '@/shared/store'
import { clientId, redirectUri, scopes } from '@/shared/constants'

export default function Index() {
  const test = useMusixStore();
  
  return (
    <>
      <div className="absolute left-0 right-0 top-0 bottom-0 flex items-center justify-center">
        <div className="flex flex-col items-center mb-40">
          <Waveform
            size={55}
            lineWeight={4}
            speed={2}
            color="black"
          />
          <h1 className="text-4xl font-semibold mt-5">Musix</h1>
        </div>
      </div>

      <button className="absolute gap-x-2 py-3 rounded-full bottom-6 left-4 right-4 bg-[#1db954]" onClick={e => {
        e.preventDefault();
        const scopesStr = scopes.join(' ');
        window.location.href= `https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopesStr}`;
      }}>
        <div className="flex items-center justify-center gap-x-1">
          <SpotifyLogo size={32} color="#fff" weight='fill' />
          <p className="text-white font-semibold">
            Login with Spotify
          </p>
        </div>
      </button>
    </>
  )
}
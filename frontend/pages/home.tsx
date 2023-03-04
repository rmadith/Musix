import Artist from '@/components/home/artist'
import Song from '@/components/home/song'
import Layout from '@/components/layouts/mobile'
import Show from '@/components/show.'
import useMusixStore from '@/shared/store'
import Link from 'next/link'
import { UsersThree, SpotifyLogo, Equalizer, ArrowBendUpRight } from 'phosphor-react'

export default function Home() {
  const user = useMusixStore(state => state.user);
  
  return (
    <div className="flex flex-col justify-between h-full w-full">
      <div>
        <p className="text-xl font-semibold">
          Welcome back, {user?.name}
        </p>
        <p className="text-sm text-gray-600 mt-1">
          Start listening now!
        </p>

        <hr className="mt-5 mb-4" />

        <div>
          <div className="flex items-center gap-x-2">
            <Equalizer size={32} />
            <span className="text-base text-gray-800">Active Sessions</span>
          </div>

          <Show
            when={user?.activeSessions.length != 0}
            fallback={<p className="text-sm text-gray-600 mt-1">You have no active sessions</p>}
          >
            <div className="mt-3">
              {user?.activeSessions.map((session) => (
                <Link key={session.id} href={`/session/${session.id}`}>
                  <div className="flex items-center justify-between border-2 px-4 py-2 rounded-lg">
                    <div>
                      <p>{session.theme}</p>
                      <p className="text-sm text-gray-600">by {
                        user.id == session.creatorId ? 'You' : session.creatorName
                      }</p>
                    </div>
                    <ArrowBendUpRight size={24} className="" />
                  </div>
                </Link>
              ))}
            </div>
          </Show>
        </div>

        <hr className="mt-5 mb-4" />

        <div>
          <div className="flex items-center gap-x-2">
            <SpotifyLogo size={32} color="#1db954" />
            <span className="text-base text-gray-800">Your Acount</span>
          </div>

          <div className="mt-3 grow-0 flex items-center gap-x-1 text-sm">
            <p className="shrink-0">User ID:</p>
            <p className="text-gray-600 truncate">{user?.id}</p>
          </div>

          <p className="text-sm mt-1">
            Email:{' '}
            <span className="text-gray-600">{user?.email}</span>
          </p>

          <p className="text-sm mt-4">
            Your Top Artists
          </p>
          <div className="flex gap-4 flex-wrap mt-2">
            {user?.topArtists.map((artist) => (
              <Artist key={artist.name} {...artist} />
            ))}
          </div>

          <p className="text-sm mt-5">
            Your Top Songs
          </p>
          <div>
            {user?.topTracks.map((song) => (
              <Song key={song.name} {...song} />
            ))}
          </div>
        </div>
      </div>
      
      <Show
        when={!user?.streaming}
        fallback={
          <div className="flex items-center justify-center gap-x-2 py-3 rounded-full bg-blue-500 opacity-50">
            <UsersThree size={24} color="#fff" weight='fill' />
            <p className="text-white font-semibold">
              Create Session
            </p>
          </div>
        }
      >
        <Link href="/create" className="mt-8">
          <div className="flex items-center justify-center gap-x-2 py-3 rounded-full bg-blue-500">
            <UsersThree size={24} color="#fff" weight='fill' />
            <p className="text-white font-semibold">
              Create Session
            </p>
          </div>
        </Link>
      </Show>
    </div>
  )
}

Home.getLayout = function getLayout(page: React.ReactElement) {
  return <Layout>{page}</Layout>;
}
import Layout from '@/components/layouts/mobile'
import { themes } from '@/shared/constants'
import useMusixStore from '@/shared/store'
import { useRouter } from 'next/router'

export default function CreateSession() {
  const router = useRouter();
  const { user, setUser } = useMusixStore();

  return (
    <>
      <p className="text-xl font-semibold">
        Select a theme, {user?.name}
      </p>

      <div className="mt-4">
        {themes.map((theme) => (
          <button
            className="mt-3 bg-slate-100 px-4 py-2 rounded-md w-full text-left"
            key={theme.id}
            onClick={() => {
              if (!user || user.streaming) return;
              // add new active session to user
              setUser({
                ...user,
                activeSessions: [
                  ...user.activeSessions,
                  { id: '123', theme: theme.name, creatorId: user.id, creatorName: user.name }
                ],
                streaming: true
              })
              router.replace(`/host?theme=${theme.id}`)
            }}
            type="button"
          >
            <p>{theme.name}</p>
          </button>
        ))}
      </div>
    </>
  )
}

CreateSession.getLayout = function getLayout(page: React.ReactElement) {
  return <Layout>{page}</Layout>;
}
import { create } from 'zustand'
import { persist } from 'zustand/middleware'
import { User } from '@/typescript/state'

interface MusixStore {
  user: User | null;
  setUser: (user: User) => void;
}

const useMusixStore = create<MusixStore>()(
  persist(
    (set) => ({
      user: {
        id: 'test-user-123',
        name: 'User',
        email: 'example@gmail.com',
        streaming: false,
        activeSessions: [],
        topArtists: [],
        topTracks: [],
      },
      setUser: (user: User) => set({ user }),
    }),
    {
      name: 'musix-store',
    }
  )
);

export default useMusixStore;
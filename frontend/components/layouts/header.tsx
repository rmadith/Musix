import { Waveform } from '@uiball/loaders'

export default function Header() {
  return (
    <header className="px-4 pt-6">
      <div className="flex items-center gap-x-2">
        <Waveform
          size={20}
          lineWeight={1.5}
          speed={2}
          color="black"
        />
        <h1 className="text-lg font-medium">Musix</h1>
      </div>
    </header>
  )
}
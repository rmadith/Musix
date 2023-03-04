import Image from "next/image"

export default function Artist({ name, image }: Props) {
  return (
    <div className="bg-slate-100 py-2 px-3 flex items-center rounded-md">
      <Image
        src={image}
        alt={name}
        width={25}
        height={25}
        className="rounded-full"
      />
      <p className="text-sm text-gray-800 ml-2">{name}</p>
    </div>
  )
}

// ------------------------------ //
// types

type Props = {
  name: string
  image: string
}
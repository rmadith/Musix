import Image from "next/image"

export default function Song({ name, image }: Props) {
  return (
    <div className="flex items-center mt-3">
      <Image
        src={image}
        alt={name}
        width={40}
        height={40}
      />
      <p className="text-sm text-gray-800 ml-2 truncate">{name}</p>
    </div>
  )
}

// ------------------------------ //
// types

type Props = {
  name: string
  image: string
}
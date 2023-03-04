import dynamic from 'next/dynamic'
import 'react-toastify/dist/ReactToastify.min.css'

export default function Toaster() {
  return (
    <ToastContainer
      position="bottom-center"
      limit={2}
      autoClose={3000}
      transition={Slide}
      hideProgressBar={true}
      closeButton={false}
      closeOnClick={false}
      style={{ padding: "20px", bottom: "0px" }}
    />
  );
}

const ToastContainer = dynamic(
  () => import('react-toastify').then((mod) => mod.ToastContainer), {
  ssr: false
});

const Slide = dynamic(
  () => import('react-toastify').then((mod) => mod.Slide), {
  ssr: false,
});
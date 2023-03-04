/**
 * Inspired by solidjs's Show component. Simplifies conditional 
 * rendering of components.
 * 
 * @param {Props} props
 * @returns {JSX.Element | null}
 */
export default function Show({
  children, when, fallback,
}: Props): JSX.Element | null {
  // basic flow control
  if (when === true) {
    return <>{children}</>;
  } else if (fallback === undefined) {
    return null;
  } else {
    return <>{fallback}</>;
  }
}

// ------------------------------ //
// types:

type Props = {
  when: boolean
  children: React.ReactNode
  fallback?: React.ReactNode
}
import React from 'react'
import Link from 'next/link'
import { useSignOut } from 'react-firebase-hooks/auth';
import { auth } from '@/firebase';
import { useRouter } from 'next/navigation';


const Menu = () => {
        const router=useRouter()
     const [signOut, loading, error] = useSignOut(auth);

  return (
   <div  >
                        
       <div className='cursor-pointer border-b-2 py-1  border-black px-8'>
        <Link href="/">Profile</Link>
        </div>

        <div className='cursor-pointer   px-8' onClick={async () => {
          const success = await signOut();
          if (success) {
            router.push('/');
          }
        }}>Logout</div>
                        
        </div>
  )
}

export default Menu
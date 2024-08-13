'use client'
import Image from 'next/image'
import Modal from './components/modal/Modal'
import Background from './components/Background/Background'
import {auth} from "@/firebase"
import { useAuthState } from 'react-firebase-hooks/auth';
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import {User} from "firebase/auth"


export default function Home() {

  const router=useRouter()
  const [user, loading, error] = useAuthState(auth);

  useEffect(()=>{
        if(user){
            router.push('/dashboard')
        }
    },[user,router])
  
  return (
    <div className='flex flex-col   items-center '>
      <Background/>
      <Modal/>
    </div>
  )
}

'use client'
import Image from 'next/image'
import React,{useState} from 'react'
import useAuthentication from '@/app/hooks/useAuthentication'
import toast from "react-hot-toast"
import { AuthError } from 'firebase/auth'
import {auth,storage} from "@/firebase"


export type Variant="REGISTER"|'LOGIN'
const Modal = () => {
    const[variant,setVariant]=useState<Variant>('LOGIN')
    const [username,setUserName]=useState("")
    const[email,setEmail]=useState("")
    const[password,setPassword]=useState("")
    const [isdisabled,setIsDisabled]=useState(false)
    const [error,setError]=useState(false)
    const {Signin,Signup} =useAuthentication({email,password,username,variant})
    


    const onSubmit=async()=>{
        if(variant=='LOGIN'){
            if(email.length==0 || password.length==0){
                toast('Credentials can not be empty !', {
  icon: '😢',
}); return 
            }
        }

          if(variant=='REGISTER'){
            if(email.length==0 || password.length==0 || username.length==0){
                toast('Credentials can not be empty !', {
  icon: '😢',
}); return 
            }
        }

        if(variant=='LOGIN'){
            Signin().then((data)=>{
                console.log(data)
                if( data =='success'){
                     toast.success('Logged In')
                  
                }else{
                     toast.error('Invalid credentials')
                }
            }).catch((error)=>{
                setError(true)
            })
        }else{
             Signup().then((data)=>{
                console.log(data)
                if(typeof data=='string'){
                     toast.success('Account created successfully ')
                  
                }else{
                     toast.error('An error occured')
                }
            }).catch((error)=>{
                setError(true)
            })
        }
    }

  return (
    <div className=' select-none z-20 mt-24 rounded-lg p-8 w-10/12  h-full  opacity-90  max-w-2xl bg-gray-100'>
        <div className=' select-none mt-3 items-center justify-center flex flex-col '>
            <Image alt="logo" height="200" width="200" className=" select-none w-[3060] h-[689]" src={'/image/bowenlogo.webp'}/>
            <p className=' mt-4 text-2xl'>{variant=='LOGIN'?"Welcome back!":'Welcome to Sshub'} &#128075;  </p>
        </div>
        <div className='flex mt-3 flex-col w-full p-2 space-y-4'>

           {variant=='LOGIN'?"":(
             <input value={username} onChange={(e)=>setUserName(e.target.value)} placeholder='Username' className=' rounded-lg px-2 outline-none  form-input block w-full border-0 py-3
          text-gray-500 shadow-sm ring-1 ring-gray-300 ring-inset
           placeholder:text-gray-400 focus:ring-2 focus:ring-inset
            focus:ring-sky-600 sm:text-md sm:leading-6' type='text'/>
           )}

            <input  value={email} onChange={(e)=>setEmail(e.target.value)} placeholder='email' className=' rounded-lg px-2 outline-none  form-input block w-full border-0 py-3
          text-gray-500 shadow-sm ring-1 ring-gray-300 ring-inset
           placeholder:text-gray-400 focus:ring-2 focus:ring-inset
            focus:ring-sky-600 sm:text-md sm:leading-6' type='email'/>


            <input  value={password} onChange={(e)=>setPassword(e.target.value)} placeholder='password'  className=' rounded-lg px-2 outline-none  form-input block w-full border-0 py-3
          text-gray-500 shadow-sm ring-1 ring-gray-300 ring-inset
           placeholder:text-gray-400 focus:ring-2 focus:ring-inset
            focus:ring-sky-600 sm:text-md sm:leading-6' type='password'/>
        </div>

        <div className=' ml-3 mt-2 flex '>
            <p>{variant=='LOGIN'?"Don't have an account?":'Already have an account?'} <span className='text-blue-700 cursor-pointer' onClick={()=>{variant=='LOGIN'?setVariant('REGISTER'):setVariant('LOGIN')}}> {variant=='LOGIN'?'Sign up':'Sign in'}</span> </p>
        </div>

        <div className='ml-3 mt-2'>
            <p className='text-red-500'>{error? "An error occured":""}</p>
        </div>

        <div  className=' mt-4 flex flex-row-reverse'>
            <button onClick={onSubmit}  className=' py-2 px-4 rounded-md text-white  bg-blue-700'>
                {variant=='LOGIN'?'Login':'Register'}
            </button>
        </div>
        
        </div>
  )
}

export default Modal
'use client'
import Link from 'next/link'
import React,{useState} from 'react'
import { CgProfile } from "react-icons/cg"
import Menu from './Menu'
import { auth } from '@/firebase'

const Topbar = () => {
    const [isOpen,setIsOpen]=useState(false)
    if(!auth.currentUser) return null
  return (
    <div className=' flex items-center flex-row-reverse justify-between  shadow-lg  p-4 w-full  pl-40 lg:pl-72'>
        
        <div className='flex items-center space-x-4 border-3'>
            <p className=' hover:text-blue-500 cursor-pointer text-sm text-gray-600'>{auth.currentUser.email? auth!.currentUser!.email as string:''}</p>
            <p className='hover:text-blue-500 cursor-pointer  text-sm text-gray-600'>400L</p>
            <div className='  relative'>
                <CgProfile onClick={()=>setIsOpen(!isOpen)} className=' mr-8  lg:mr-10 hover:text-blue-500 cursor-pointer h-10 w-10' />
                <div className='  rounded-lg  top-[60px]  bg-white border-black border-1  right-5 absolute  '>
                    
                   {isOpen? (
                    <Menu/>
                   ) :""}
                </div>
            </div>
            
        </div>
        </div>
  )
}

export default Topbar
'use client'

import React from 'react'

import Link from "next/link"


type DesktopItemProps={
label:string
icon : any
href:string
onClick?:()=>void;
active?:boolean
}
const DesktopItem:React.FC<DesktopItemProps> = ({label,icon:Icon,href,onClick,active}) => {
  const handleClick=()=>{
    if(onClick){
      return onClick()
    }
  }
  return (
    <li onClick={handleClick} >
        <Link className='   gap-x-3 rounded-md p-3 text-sm leading-6 font-semibold text-slate-300   mt-5  flex flex-col lg:flex-row  group ' href={href}>
         <Icon className={`h-6 w-6  shrink-0  group-hover:text-white ${active ? "text-black":"text-slate-300"} `}/>
         <p className="text-sm group-hover:text-white">{label}</p>
        </Link>
    </li>
  )
}

export default DesktopItem



import React from 'react'
import DesktopSidebar from './DesktopSidebar'
import Topbar from './Topbar'

const Sidebar = ({children}:{children:React.ReactNode}) => {
  return (
    <div className='h-full'>
        <Topbar/>
        <DesktopSidebar/>
    <main className="lg:pl-20 h-full">

            {children}
        </main>
        </div>
  )
}

export default Sidebar
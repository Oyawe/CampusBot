"use client";

import React, { useState } from "react";
import { IoIosSpeedometer } from "react-icons/io";
import { IoDocumentText } from "react-icons/io5";
import { BsFillHousesFill } from "react-icons/bs";
import { ImStatsBars } from "react-icons/im";
import { BsTicketDetailedFill } from "react-icons/bs";
import { FaFolder, FaMusic, FaBook, FaVoteYea } from "react-icons/fa";
import DesktopItem from "./DesktopItem";
// import useRoutes from '@/app/hooks/useRoute'
// import DesktopItem from './DesktopItem'
// import { User } from '@prisma/client'
// import Avatar from "./Avatar"

// interface DesktopSidebarProps{
//   currentUser:User
// }
const DesktopSidebar = () => {
  //   const routes=useRoutes()
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div
      className=" w-32 fixed inset-y-0 left-0 z-40 lg:w-60
    px-1 lg:px-3 overflow-y-auto bg-blue-500 border-r-[1px] pb-4 flex
     flex-col justify-between "
    >
      <nav className=" mt-4 overflow-y-scroll no-scrollbar   flex flex-col justify-between">
        <ul
          role="list"
          className="   flex flex-col items-start justify-center space-y-1"
        >
          <h1 className="flex pt-2 justify-center text-xl text-gray-300 font-bold">
            Students Dashboard
          </h1>
          <DesktopItem
            label="Dahboard"
            icon={IoIosSpeedometer}
            href="/dashboard"
          />
          <DesktopItem
            label="Course Registration"
            icon={IoDocumentText}
            href="/dashboard"
          />
          <DesktopItem
            label="Hostel Management"
            icon={BsFillHousesFill}
            href="/dashboard"
          />
          <DesktopItem
            label="Result processing"
            icon={ImStatsBars}
            href="/dashboard"
          />
          <DesktopItem
            label="Profile"
            icon={IoIosSpeedometer}
            href="/dashboard"
          />
          <DesktopItem
            label="Payment"
            icon={BsTicketDetailedFill}
            href="/dashboard"
          />
          <DesktopItem label="My Courses" icon={FaFolder} href="/dashboard" />
          <DesktopItem label="Bowen Anthem" icon={FaMusic} href="/dashboard" />
          <DesktopItem
            label="Student Handbook"
            icon={FaBook}
            href="/dashboard"
          />
          <DesktopItem
            label="BBSF Election"
            icon={FaVoteYea}
            href="/dashboard"
          />
        </ul>
      </nav>

      <nav className="mt-4 flex flex-col justify-between items-center">
        {/* <div
            className='cursor-pointer hover:opacity-75 trabsition'
            onClick={()=>setIsOpen(true)}>
                <Avatar user={currentUser}/>
            </div> */}
      </nav>
    </div>
  );
};

export default DesktopSidebar;

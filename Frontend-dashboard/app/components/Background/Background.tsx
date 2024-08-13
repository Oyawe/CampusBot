'use client'
import React,{useState,useEffect} from 'react'

const Background = () => {
    const[count,setCount]=useState(0)
    const images:string[]=['https://bowen.edu.ng/wp-content/uploads/2023/04/Web-17-1024x683.jpg?lm=643E975C',"https://bowen.edu.ng/wp-content/uploads/2023/04/Web-31.jpg?lm=643E9771","https://bowen.edu.ng/wp-content/uploads/2023/04/faith-1024x682.png?lm=643FE159","https://bowen.edu.ng/wp-content/uploads/2023/04/sport-1024x683.png?lm=643FE1AD","https://bowen.edu.ng/wp-content/uploads/2023/04/Web-5-1024x683.jpg?lm=643E77EF"]
  useEffect(() => {
    // This effect runs on mount
    const intervalId = setInterval(() => {
      // Update the count every 1000 milliseconds (1 second)
      setCount(prevIndex => (prevIndex + 1) % images.length);
    }, 10000);

    



    // Clear the interval when the component unmounts
    return () => {
      clearInterval(intervalId);
    };
  }, []);
    return (

    <div className='fixed'>
        <img className='h-screen w-screen  object-cover  ' src={images[count]} alt='image'/>
    </div>
  )
}

export default Background
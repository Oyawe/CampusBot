'use client'
import { Variant } from '@/app/components/modal/Modal';
import { auth, db } from '@/firebase';
import React from 'react'
import { useCreateUserWithEmailAndPassword } from 'react-firebase-hooks/auth';
import { useSignInWithEmailAndPassword } from 'react-firebase-hooks/auth';

import { doc, setDoc } from "firebase/firestore"; 



interface Props{
  email:string;
  password:string;
  username:string
  variant:Variant
}
const useAuthentication = ({email,password,username,variant}:Props) => {

  const [
  createUserWithEmailAndPassword,
  user,
  loading,
  error,
] = useCreateUserWithEmailAndPassword(auth);

const [
  signInWithEmailAndPassword,
  user2,
  loading2,
  error2,
] = useSignInWithEmailAndPassword(auth);

const Signup=async()=>{
  try{
    await createUserWithEmailAndPassword(email, password)
    // if(loading) return loading
    if(error)  return error
    // Add a new document in collection "cities"
  await setDoc(doc(db, "users", email), {
  name: username,
  email:email,
  createdAt:new Date()
});
    return "success"
  }catch(e:any){
    return error
  }
}

const Signin=async()=>{
  try{
  await signInWithEmailAndPassword(email, password)
  if(error2) return error2
  if(loading2) return 'loading'
  return "success"
  }
  catch(e){
    return error2
  }
}

 return {Signin,Signup}
  
}

export default useAuthentication
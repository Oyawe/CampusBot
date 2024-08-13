// Import the functions you need from the SDKs you need
import { initializeApp,getApp,getApps } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth} from "firebase/auth"
import {getFirestore} from "firebase/firestore"
import {getStorage} from "firebase/storage" 
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAsL39elYAX_4AIcCw1uJSkslGMrDUGiCw",
  authDomain: "sshub-1cc22.firebaseapp.com",
  projectId: "sshub-1cc22",
  storageBucket: "sshub-1cc22.appspot.com",
  messagingSenderId: "1020002056408",
  appId: "1:1020002056408:web:e372ca47ba9b7461123fad",
  measurementId: "G-RHPGTGVQ9V"
};

// Initialize Firebase
const app = !getApps.length ?  initializeApp(firebaseConfig) : getApp();
// const analytics = getAnalytics(app);
const auth=getAuth(app)
const db=getFirestore(app)
const storage=getStorage(app);

export {auth,db,storage,app}
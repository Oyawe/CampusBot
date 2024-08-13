"use client";
import React, { useEffect } from "react";
import Card from "./components/Card";
import { auth } from "@/firebase";
import { useAuthState } from "react-firebase-hooks/auth";
import { useRouter } from "next/navigation";

// custom.d.ts
declare namespace JSX {
  interface IntrinsicElements {
    "df-messenger": any;
  }
}

const Index = () => {
  const router = useRouter();
  const [user, loading, error] = useAuthState(auth);

  useEffect(() => {
    if (user) {
      router.push("/dashboard");
    }
  }, [user, router]);

  useEffect(() => {
    const script = document.createElement("script");
    script.src =
      "https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1";
    script.async = true;
    document.body.appendChild(script);
    return () => {
      document.body.removeChild(script);
    };
  }, []);

  return (
    <div className="flex flex-col lg:flex-row mt-10 pl-40 lg:pl-52 gap-8 flex-wrap">
      <div className="flex flex-col lg:flex-row flex-wrap gap-8">
        <Card label="Course Registration" color="red" />
        <Card label="Hostel Management" color="blue" />
        <Card label="Result Processing" color="slate" />
        <Card label="E-Learnng" color="blue" />
        <Card label="Payment" color="sate" />
        <Card label="My Courses" color="red" />
        <Card label="Bowen Anthem" color="slate" />
        <Card label="Student Handbook" color="red" />
        <Card label="BBSF Election" color="blue" />
      </div>
      <div className="mt-10 lg:mt-0 lg:ml-10">
        <df-messenger
          chat-icon="https:&#x2F;&#x2F;i.postimg.cc&#x2F;yx5qpQ84&#x2F;pngwing-com.png"
          intent="WELCOME"
          chat-title="CampusBot(Students)🤖"
          agent-id="4a001c7e-6be2-4bf0-b7e6-57cf4839901e"
          language-code="en"
        ></df-messenger>
      </div>
    </div>
  );
};

export default Index;

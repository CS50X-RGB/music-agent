"use client"
import Input_ from "@/components/resuables/Input/page";
import { Button } from "@heroui/react";
import { useState } from "react";

export default function Register() {
    const [form, setForm] = useState({
        email: "",
        password: "",
        name : ""
    });
    const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
        e.preventDefault();
    };
    return (
        <div className="flex flex-col p-8 gap-4 rounded-2xl border border-[rgba(199,243,107,0.16)] bg-[rgba(20,23,20,0.65)] backdrop-blur-xl shadow-[0_8px_32px_rgba(0,0,0,0.25)]">
            <h1 className="max-w-4xl text-4xl font-bold tracking-tight text-accent sm:text-3xl md:text-5xl">
                Welcome 
            </h1>
            <p className="max-w-xl text-base text-default-500 sm:text-lg">
                Sign up to your account to continue your music journey.
            </p>
            <form onSubmit={(e) => handleSubmit(e)} className="flex flex-col gap-4 p-4">
                <Input_ type="text" placeholder="Rohan" state={form} setState={setForm} name="name" />
                <Input_ type="email" placeholder="johndoe@gmail.com" state={form} setState={setForm} name="email" />
                <Input_ type="password" placeholder="abcd!23" state={form} setState={setForm} name="password" />
                <Button size="lg" className={"w-full text-black"}>Submit</Button>
            </form>
        </div>
    )   
}
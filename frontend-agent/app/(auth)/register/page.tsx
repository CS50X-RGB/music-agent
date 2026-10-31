"use client"
import Input_ from "@/components/resuables/Input/page";
import { Button, toast } from "@heroui/react";
import { useState } from "react";
import { useMutation } from "@tanstack/react-query";
import { postData } from "@/core/api/apiHandler";
import { clientToken,currentUser } from "@/core/api/localStorageKeys";
import { accountRoutes } from "@/core/api/apiRoutes";
import { UserRegister } from "@/types/states";
import { useRouter } from "next/navigation";
import { AxiosError } from "axios";
import { ValidationError } from "@/types/error";


export default function Register() {
    const [form, setForm] = useState<UserRegister>({
        email: "",
        password: "",
        name: ""
    });
    const [errMsg,setErrMsg] = useState<string | null>('');
    
    const router  = useRouter();
    const registerMutate = useMutation({
        mutationKey: ["register"],
        mutationFn: async (data: UserRegister) => {
            return await postData(accountRoutes.register, {}, data);
        },
        onError: (error: AxiosError<ValidationError | { detail: string }>) => {
            const detail = error.response?.data?.detail;

            if (Array.isArray(detail)) {
                setErrMsg(
                    detail
                        .map((err) => `${err.msg} for ${err.loc.at(-1)}`)
                        .join(", ")
                );
            } else if (typeof detail === "string") {
                setErrMsg(detail);
            } else {
                setErrMsg(error.message || "Something went wrong");
            }
        },
        onSuccess: (data: unknown) => {
            const response = data as {
                data: {
                    access_token: string;
                    token_type: string;
                    user: {
                        id: string;
                        name: string;
                        email: string;
                    }
                }
            }

            const { access_token,user } = response.data;
            localStorage.setItem(clientToken,access_token);
            localStorage.setItem(currentUser,JSON.stringify(user));
            toast.success('Registered Sucessful!')
            router.push('/dashboard');
        }
    });

    const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
        e.preventDefault();
        registerMutate.mutate(form);
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
                <Button type="submit" size="lg" className={"w-full text-black"}>Submit</Button>
            </form>
        </div>
    ) 
}
"use client"
import Input_ from "@/components/resuables/Input/page";
import { postData } from "@/core/api/apiHandler";
import { accountRoutes } from "@/core/api/apiRoutes";
import { clientToken } from "@/core/api/localStorageKeys";
import { ValidationError } from "@/types/error";
import { UserLogin } from "@/types/states";
import { Button, toast } from "@heroui/react";
import { useMutation } from "@tanstack/react-query";
import { AxiosError } from "axios";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Login() {
    const [form, setForm] = useState<UserLogin>({
        email: "",
        password: ""
    });
    const router = useRouter();

    const loginMutate = useMutation({
        mutationKey: ["login"],
        mutationFn: async (data: UserLogin) => {
            return await postData(accountRoutes.login, {}, data);
        },
        onError: (error: AxiosError<ValidationError | { detail: string }>) => {
            const detail = error.response?.data?.detail;
            console.log(detail)
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

            toast.success('Login Sucessful!')
            router.push('/dashboard');
        }
    });
    const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("Here")
        loginMutate.mutate(form);
    };
    return (
        <div className="flex flex-col p-8 gap-4 rounded-2xl border border-[rgba(199,243,107,0.16)] bg-[rgba(20,23,20,0.65)] backdrop-blur-xl shadow-[0_8px_32px_rgba(0,0,0,0.25)]">
            <h1 className="max-w-4xl text-4xl font-bold tracking-tight text-accent sm:text-3xl md:text-5xl">
                Welcome back
            </h1>
            <p className="max-w-xl text-base text-default-500 sm:text-lg">
                Sign in to your account to continue your music journey.
            </p>
            <form onSubmit={(e)=> handleSubmit(e)} className="flex flex-col gap-4 p-4">
                <Input_ type="email" placeholder="johndoe@gmail.com" state={form} setState={setForm} name="email" />
                <Input_ type="password" placeholder="abcd!23" state={form} setState={setForm} name="password" />
                <Button type="submit" size="lg" className={"w-full text-black"}>Submit</Button>
            </form>
        </div>
    )   
}
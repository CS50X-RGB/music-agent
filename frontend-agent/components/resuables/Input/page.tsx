import { Label, Input } from "@heroui/react"
import React from "react";

type InputProps<T extends Record<string, string>> = {
    state: T,
    setState: React.Dispatch<React.SetStateAction<T>>;
    name: keyof T;
    type?: "text" | "email" | "number" | "password",
    placeholder: string
}

export default function Input_<T extends Record<string, string>>({ state, name, setState, type, placeholder }: InputProps<T>) {
    const fieldName = String(name);
    const inputId = `input-type-${fieldName}`;
    const strVal = String(placeholder)
    return (
        <div className="flex flex-col items-start text-[rgba(199,243,107)] p-4 gap-2">
            <Label className="text-[rgba(199,243,107)]" htmlFor={inputId}>  {fieldName.charAt(0).toUpperCase() + fieldName.slice(1)}</Label>
            <Input
                className="w-full rounded-xl border
                border-[rgba(199,243,107,0.16)]
                bg-[rgba(20,23,20,0.65)] 
                text-[rgba(199,243,107)]"
                id={inputId}
                size={10}
                value={String(state[name])}
                onChange={(e) => setState((prev) => ({
                    ...prev,
                    [name]: e.target.value
                }))}
                placeholder={strVal} type={type} />
        </div>
    )
}
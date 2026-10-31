'use client'
import { postData } from "@/core/api/apiHandler";
import { agentRoutes } from "@/core/api/apiRoutes";
import { Label, TextArea, Button } from "@heroui/react";
import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { HiSparkles } from "react-icons/hi2";

export default function PromptInput() {
    const [prompt, setPrompt] = useState<string>("");
    const promptAgent = useMutation({
        mutationKey : ["promptAgent"],
        mutationFn : (data : { prompt : string }) => {
            return postData(agentRoutes.generate,{},data);
        }
    });

    const handleSubmit = (e: React.SubmitEvent<HTMLFormElement>) => {
        e.preventDefault();
        const data : {prompt : string} = {
            prompt : prompt
        }
        promptAgent.mutate(data);
    };
    return (
        <div className="w-full max-w-3xl rounded-2xl border border-[rgba(199,243,107,0.16)] bg-[rgba(20,23,20,0.65)] p-5 shadow-[0_8px_32px_rgba(0,0,0,0.25)] backdrop-blur-xl sm:p-6">
            <div className="mb-4 flex items-center justify-between gap-3">
                <div className="flex flex-col gap-1">
                    <h2 className="text-lg font-semibold text-[rgba(199,243,107)]">
                        Describe your vibe
                    </h2>
                    <p className="text-sm text-default-500">
                        Tell AI what you want to listen to.
                    </p>
                </div>

                <HiSparkles className="h-6 w-6 shrink-0 text-[rgba(199,243,107)]" />
            </div>

            <form
            onSubmit={(e) => handleSubmit(e)}
            className="flex flex-col gap-4"
        >
            <Label
                htmlFor="playlist-prompt"
                className="text-sm font-medium text-foreground"
            >
                Prompt message
            </Label>

            <TextArea
                id="playlist-prompt"
                name="prompt"
                placeholder="e.g. Late-night driving, dark trap beats, Playboi Carti vibes..."
                rows={5}
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                className="w-full rounded-xl border border-[rgba(199,243,107,0.16)] bg-[rgba(20,23,20,0.65)] text-[rgba(199,243,107)] placeholder:text-default-500"
            />

            <div className="mt-2 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                <p className="text-xs text-default-500">
                    Be specific about artists, mood, or genre.
                </p>

                <Button
                    type="submit"
                    isDisabled={!prompt?.trim()}
                    className="font-semibold text-black"
                >
                    <HiSparkles className="h-4 w-4" />
                    Generate playlist
                </Button>
            </div>
        </form>

        </div>
    );
}

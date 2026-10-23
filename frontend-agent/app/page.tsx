import Hero from "@/components/hero/page";
import Navbar from "@/components/navbar/page";
import { Suspense } from "react";

export default function Home() {
  return (
    <>
      <div className="flex flex-col flex-1 items-center justify-center font-sans">
        <Hero />
      </div>
    </>
  );
}

import Hero from "@/components/hero/page";
import Navbar from "@/components/navbar/page";

export default function Home() {
  return (
    <>
      <Navbar>
        <div className="flex flex-col flex-1 items-center justify-center font-sans">
          <Hero />
        </div>
      </Navbar>
    </>
  );
}

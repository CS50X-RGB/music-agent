import { Button } from "@heroui/react";

export default function Hero() {
  return (
    <section className="flex min-h-[70vh] flex-col items-center justify-center gap-6 px-4 text-center">
      <h1 className="max-w-4xl text-4xl font-bold tracking-tight text-accent sm:text-5xl md:text-6xl">
        Describe the artist or vibe.
        <span className="block mt-2">
          We&apos;ll build your playlist.
        </span>
      </h1>

      <p className="max-w-xl text-base text-default-500 sm:text-lg">
        Tell us what you&apos;re feeling, and let AI discover your next
        favorite tracks.
      </p>

      <Button
        size="lg"
        // color="primary"
        className="font-semibold"
        // onPress={() => {
        //   window.location.href = "/login";
        // }}
      >
        Create Your Playlist
      </Button>
    </section>
  );
}

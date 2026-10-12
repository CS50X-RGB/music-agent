export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
        <section className="rounded-xl border border-border bg-surface p-6">
          <h1 className="font-sans text-3xl font-bold">
            Your mood, in a playlist.
          </h1>

          <p className="mt-2 text-muted">
            Discover your next favorite sound.
          </p>

          <button className="mt-4 rounded-lg bg-accent px-5 py-3 font-semibold text-background">
            Generate playlist
          </button>
        </section>
    </div>
  );
}

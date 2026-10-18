export default function Dashboard() {
    return (
        <>
            <div className="flex flex-col gap-4 p-5">
                <h2 className="text-3xl text-bold">Good Morning,Rohan !</h2>
                <p>Here is what is new for you.</p>
            </div>
            <div className="bg-linear-tr from-[rgb(199,243,107)] to-blue-400 border-4 border-blue-400">
                <h3 className="text-xl">Create a New Playlist</h3>
            </div>
        </>
    );
}

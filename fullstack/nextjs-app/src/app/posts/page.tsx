import prisma from "../../lib/db";
import Link from "next/link";

export default async function PostsPage() {
    const users = await prisma.users.findMany();

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">All Posts (0)</h1>

            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {users.map((user) => (
                    <li key={user.id} className="flex items-center justify-between px-5">
                        <Link href={`/posts/${user.id}`}>{user.email}</Link>
                    </li>
                ))}
            </ul>
        </main>
    )
}
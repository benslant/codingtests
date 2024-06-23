import prisma from "../../lib/db";
import Link from "next/link";
import { createUser } from "../../actions/actions"

export default async function UsersPage() {
    const users = await prisma.user?.findMany();
    const userCount = await prisma.user?.count()

    return (
        <main className="flex flex-col items-center gap-y-5 pt-24 tex-center">
            <h1 className="text-3xl find0semi-bold">All Users ({userCount})</h1>

            <ul className="border-t border-b border-black/10 py-5 leading-8">
                {users?.map((user) => (
                    <li key={user.id} className="flex items-center justify-between px-5">
                        <Link href={`/user/${user.id}`}>{user.email}</Link>
                    </li>
                ))}
            </ul>

            <form action={createUser} className="flex flex-col gap-y-2 w-[300px]">
                <input
                    type="text"
                    name="first_name"
                    placeholder="First Name"
                    className="px-2 py1 rounded-sm font-black"
                    />
                <input
                    type="text"
                    name="last_name"
                    placeholder="Last Name"
                    className="px-2 py1 rounded-sm font-black"
                    />
                <input
                    type="text"
                    name="email"
                    placeholder="Email"
                    className="px-2 py1 rounded-sm font-black"
                    />
                <button type="submit" className="bg-blue-500 text-white rounded-sm">
                    Create User
                </button>
            </form>
        </main>
    )
}
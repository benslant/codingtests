'use server';

import { revalidatePath } from 'next/cache';
import prisma from '../lib/db'
import {v4 as uuidv4} from 'uuid';

export async function createUser(formData: FormData) {
    try {
    await prisma.user.create({
        data: {
            first_name: formData.get("first_name") as string,
            last_name: formData.get("last_name") as string,
            email: formData.get("email") as string,
            id: uuidv4()  
        }
    })
} catch(error){
    console.log(error)
}

    revalidatePath('/user');
}

export async function createGroup(formData: FormData) {
    try {
    await prisma.group.create({
        data: {
            name: formData.get("group_name") as string,
            id: uuidv4()  
        }
    })
    } catch(error) {
        console.log(error)
    } 

    revalidatePath('/group');
}
import { use } from "react";
import Parse from "../back4app";


export async function register(
    username: string, password: string) {
    const user = new Parse.User();

    user.set('username', username);
    user.set('password', password);

    await user.signUp()
    return user;
}

export async function login(username: string, password: string) {
    const user = await Parse.User.logIn(username, password);
    return user;
}

export async function logout() {
    await Parse.User.logOut();
}

export async function getCurrectUser() {
    return await Parse.User.currentAsync();
}

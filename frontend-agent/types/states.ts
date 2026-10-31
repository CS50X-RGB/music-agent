export type UserRegister = {
    name : string,
    email : string,
    password : string
}
export type UserLogin = {
    email : string,
    password : string
}

export interface User{
    name : string,
    id : string,
    email : string
}
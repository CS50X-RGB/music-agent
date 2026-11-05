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

export type AgentResponse = {
    data : {
        msg : Record<string,string>,
        status : number
    }
}
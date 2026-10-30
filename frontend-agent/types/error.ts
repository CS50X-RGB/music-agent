export interface ValidationError {
    detail: {
        type: string;
        loc: (string | number)[];
        msg: string;
        input: unknown;
        ctx?: {
            min_length?: number;
        };
    }[];
}
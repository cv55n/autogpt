import { type NextRequest } from "next/server";

import { updateSession } from "@/lib/supabase/middleware";

export async function middleware(request: NextRequest) {
    return await updateSession(request);
}

export const config = {
    /**
     * corresponde a todos os caminhos de solicitação, exceto aqueles que começam com
     * 
     * - _next/static (arquivos estáticos)
     * - _next/image (arquivos de otimização de imagem)
     * - favicon.ico (arquivo favicon)
     * 
     * sinta-se à vontade para modificar este padrão para incluir mais paths
     */
    matcher: [
        "/((?!_next/static|_next/image|favicon.ico|auth|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)"
    ]
};
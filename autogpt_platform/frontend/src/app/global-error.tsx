"use client";

import * as Sentry from "@sentry/nextjs";
import NextError from "next/error";
import { useEffect } from "react";

export default function GlobalError({
    error
}: {
    error: Error & { digest?: string };
}) {
    useEffect(() => {
        Sentry.captureException(error);
    }, [error]);

    return (
        <html>
            <body>
                {/* `nexterror` é o componente de erro padrão do next.js */}

                <NextError statusCode={0} />
            </body>
        </html>
    );
}
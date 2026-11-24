import { getData } from "@/core/api/apiHandler";
import { accountRoutes } from "@/core/api/apiRoutes";
import { clientToken } from "@/core/api/localStorageKeys";
import { useQuery } from "@tanstack/react-query";
import { usePathname } from "next/navigation";

export default function useAuth() {
  const hasToken = typeof window !== "undefined" && !!localStorage.getItem(clientToken);
  const pathname = usePathname();
  const isPublicRoute = ["/", "/login", "/register"].includes(pathname);
  const {
    data: accountData,
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ["get-profile"],
    queryFn: () => {
      return getData(accountRoutes.profile, {});
    },
    enabled: hasToken && !isPublicRoute,
  });

  return {
    accountData,
    isLoading,
    isError,
    error,
  };
}

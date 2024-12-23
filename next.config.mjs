/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: true,
    rewrites: async () => {
      return [
        {
          source: "/api/:path*/",
          destination:
            process.env.NODE_ENV === "development"
              ? "http://127.0.0.1:8000/api/:path*/"
              : "/api/",
        },
        {
          source: "/docs",
          destination:
            process.env.NODE_ENV === "development"
              ? "http://127.0.0.1:8000/docs"
              : "/api/docs",
        },
      ];
    },
  };
  
export default nextConfig;
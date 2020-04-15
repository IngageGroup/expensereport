#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["./backend/expensereport-api/expensereport-api.csproj", "./backend/expensereport-api/"]
RUN dotnet restore "./backend/expensereport-api/expensereport-api.csproj"
COPY . .
WORKDIR "/src/backend/expensereport-api"
RUN ls
RUN dotnet build "expensereport-api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "expensereport-api.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "expensereport-api.dll"]
from typing import List
from entities.package import Package
from models.package_model import PackageModel

class PackageRepository:
    def save(self, package: Package) -> None:
        package_model = PackageModel()
        package_dict = package.model_dump()

        for k in PackageModel.get_normal_fields():
            if k not in package_dict:
                continue
            package_model[k] = package_dict[k]

        package_model.save()

    def get_package_by_id(self, package_id: str) -> dict:
        package = PackageModel.objects(id=package_id).first()
        if not package:
            return None
        package_dict = package.to_mongo().to_dict()
        package_dict["_id"] = str(package_dict["_id"])
        return package_dict

    def list_all_packages(self) -> List[dict]:
        packages = PackageModel.objects()
        return [
            {
                **package.to_mongo().to_dict(),
                "_id": str(package.id)
            }
            for package in packages
        ]

    def delete_package(self, package_id: str) -> None:
        package = PackageModel.objects(id=package_id).first()
        if not package:
            raise ValueError("Pacote não encontrado para exclusão.")
        package.delete()

    def update_package(self, package_id: str, updated_fields: dict) -> None:
        package = PackageModel.objects(id=package_id).first()
        if not package:
            raise ValueError("Pacote não encontrado para atualização.")
        
        for field, value in updated_fields.items():
            setattr(package, field, value)

        package.save()

    def find_by_id(self, package_id: str):
        return PackageModel.objects(id=package_id).first()

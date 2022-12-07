from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app = lazy_import('msgraph.generated.models.mobile_app')
win_get_app_install_experience = lazy_import('msgraph.generated.models.win_get_app_install_experience')

class WinGetApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WinGetApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.winGetApp"
        # The install experience settings associated with this application, which are used to ensure the desired install experiences on the target device are taken into account. This includes the account type (System or User) that actions should be run as on target devices. Required at creation time.
        self._install_experience: Optional[win_get_app_install_experience.WinGetAppInstallExperience] = None
        # Hash of package metadata properties used to validate that the application matches the metadata in the source repository.
        self._manifest_hash: Optional[str] = None
        # The PackageIdentifier from the WinGet source repository REST API. This also maps to the Id when using the WinGet client command line application. Required at creation time, cannot be modified on existing objects.
        self._package_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WinGetApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WinGetApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WinGetApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "install_experience": lambda n : setattr(self, 'install_experience', n.get_object_value(win_get_app_install_experience.WinGetAppInstallExperience)),
            "manifest_hash": lambda n : setattr(self, 'manifest_hash', n.get_str_value()),
            "package_identifier": lambda n : setattr(self, 'package_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_experience(self,) -> Optional[win_get_app_install_experience.WinGetAppInstallExperience]:
        """
        Gets the installExperience property value. The install experience settings associated with this application, which are used to ensure the desired install experiences on the target device are taken into account. This includes the account type (System or User) that actions should be run as on target devices. Required at creation time.
        Returns: Optional[win_get_app_install_experience.WinGetAppInstallExperience]
        """
        return self._install_experience
    
    @install_experience.setter
    def install_experience(self,value: Optional[win_get_app_install_experience.WinGetAppInstallExperience] = None) -> None:
        """
        Sets the installExperience property value. The install experience settings associated with this application, which are used to ensure the desired install experiences on the target device are taken into account. This includes the account type (System or User) that actions should be run as on target devices. Required at creation time.
        Args:
            value: Value to set for the installExperience property.
        """
        self._install_experience = value
    
    @property
    def manifest_hash(self,) -> Optional[str]:
        """
        Gets the manifestHash property value. Hash of package metadata properties used to validate that the application matches the metadata in the source repository.
        Returns: Optional[str]
        """
        return self._manifest_hash
    
    @manifest_hash.setter
    def manifest_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the manifestHash property value. Hash of package metadata properties used to validate that the application matches the metadata in the source repository.
        Args:
            value: Value to set for the manifestHash property.
        """
        self._manifest_hash = value
    
    @property
    def package_identifier(self,) -> Optional[str]:
        """
        Gets the packageIdentifier property value. The PackageIdentifier from the WinGet source repository REST API. This also maps to the Id when using the WinGet client command line application. Required at creation time, cannot be modified on existing objects.
        Returns: Optional[str]
        """
        return self._package_identifier
    
    @package_identifier.setter
    def package_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the packageIdentifier property value. The PackageIdentifier from the WinGet source repository REST API. This also maps to the Id when using the WinGet client command line application. Required at creation time, cannot be modified on existing objects.
        Args:
            value: Value to set for the packageIdentifier property.
        """
        self._package_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("installExperience", self.install_experience)
        writer.write_str_value("manifestHash", self.manifest_hash)
        writer.write_str_value("packageIdentifier", self.package_identifier)
    


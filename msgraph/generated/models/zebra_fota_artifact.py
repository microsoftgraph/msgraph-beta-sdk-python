from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ZebraFotaArtifact(entity.Entity):
    """
    Describes a single artifact for a specific device model.
    """
    @property
    def board_support_package_version(self,) -> Optional[str]:
        """
        Gets the boardSupportPackageVersion property value. The version of the Board Support Package (BSP. E.g.: 01.18.02.00)
        Returns: Optional[str]
        """
        return self._board_support_package_version
    
    @board_support_package_version.setter
    def board_support_package_version(self,value: Optional[str] = None) -> None:
        """
        Sets the boardSupportPackageVersion property value. The version of the Board Support Package (BSP. E.g.: 01.18.02.00)
        Args:
            value: Value to set for the boardSupportPackageVersion property.
        """
        self._board_support_package_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new zebraFotaArtifact and sets the default values.
        """
        super().__init__()
        # The version of the Board Support Package (BSP. E.g.: 01.18.02.00)
        self._board_support_package_version: Optional[str] = None
        # Artifact description. (e.g.: `LifeGuard Update 98 (released 24-September-2021)
        self._description: Optional[str] = None
        # Applicable device model (e.g.: TC8300)
        self._device_model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Artifact OS version (e.g.: 8.1.0)
        self._os_version: Optional[str] = None
        # Artifact patch version (e.g.: U00)
        self._patch_version: Optional[str] = None
        # Artifact release notes URL (e.g.: https://www.zebra.com/<filename.pdf>)
        self._release_notes_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaArtifact
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaArtifact()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Artifact description. (e.g.: `LifeGuard Update 98 (released 24-September-2021)
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Artifact description. (e.g.: `LifeGuard Update 98 (released 24-September-2021)
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. Applicable device model (e.g.: TC8300)
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. Applicable device model (e.g.: TC8300)
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "board_support_package_version": lambda n : setattr(self, 'board_support_package_version', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "patch_version": lambda n : setattr(self, 'patch_version', n.get_str_value()),
            "release_notes_url": lambda n : setattr(self, 'release_notes_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Artifact OS version (e.g.: 8.1.0)
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Artifact OS version (e.g.: 8.1.0)
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def patch_version(self,) -> Optional[str]:
        """
        Gets the patchVersion property value. Artifact patch version (e.g.: U00)
        Returns: Optional[str]
        """
        return self._patch_version
    
    @patch_version.setter
    def patch_version(self,value: Optional[str] = None) -> None:
        """
        Sets the patchVersion property value. Artifact patch version (e.g.: U00)
        Args:
            value: Value to set for the patchVersion property.
        """
        self._patch_version = value
    
    @property
    def release_notes_url(self,) -> Optional[str]:
        """
        Gets the releaseNotesUrl property value. Artifact release notes URL (e.g.: https://www.zebra.com/<filename.pdf>)
        Returns: Optional[str]
        """
        return self._release_notes_url
    
    @release_notes_url.setter
    def release_notes_url(self,value: Optional[str] = None) -> None:
        """
        Sets the releaseNotesUrl property value. Artifact release notes URL (e.g.: https://www.zebra.com/<filename.pdf>)
        Args:
            value: Value to set for the releaseNotesUrl property.
        """
        self._release_notes_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("boardSupportPackageVersion", self.board_support_package_version)
        writer.write_str_value("description", self.description)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_str_value("patchVersion", self.patch_version)
        writer.write_str_value("releaseNotesUrl", self.release_notes_url)
    


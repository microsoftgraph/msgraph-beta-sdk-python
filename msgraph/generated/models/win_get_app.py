from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app, win_get_app_install_experience

from . import mobile_app

@dataclass
class WinGetApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.winGetApp"
    # The install experience settings associated with this application, which are used to ensure the desired install experiences on the target device are taken into account. This includes the account type (System or User) that actions should be run as on target devices. Required at creation time.
    install_experience: Optional[win_get_app_install_experience.WinGetAppInstallExperience] = None
    # Hash of package metadata properties used to validate that the application matches the metadata in the source repository.
    manifest_hash: Optional[str] = None
    # The PackageIdentifier from the WinGet source repository REST API. This also maps to the Id when using the WinGet client command line application. Required at creation time, cannot be modified on existing objects.
    package_identifier: Optional[str] = None
    
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
        from . import mobile_app, win_get_app_install_experience

        fields: Dict[str, Callable[[Any], None]] = {
            "installExperience": lambda n : setattr(self, 'install_experience', n.get_object_value(win_get_app_install_experience.WinGetAppInstallExperience)),
            "manifestHash": lambda n : setattr(self, 'manifest_hash', n.get_str_value()),
            "packageIdentifier": lambda n : setattr(self, 'package_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    


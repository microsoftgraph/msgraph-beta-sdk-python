from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import agreement_file_properties, agreement_file_version

from . import agreement_file_properties

@dataclass
class AgreementFileLocalization(agreement_file_properties.AgreementFileProperties):
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Customized versions of the terms of use agreement in the Azure AD tenant.
    versions: Optional[List[agreement_file_version.AgreementFileVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementFileLocalization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFileLocalization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AgreementFileLocalization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import agreement_file_properties, agreement_file_version

        from . import agreement_file_properties, agreement_file_version

        fields: Dict[str, Callable[[Any], None]] = {
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(agreement_file_version.AgreementFileVersion)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("versions", self.versions)
    


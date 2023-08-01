from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..physical_address import PhysicalAddress

@dataclass
class SslCertificateEntity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The address property
    address: Optional[PhysicalAddress] = None
    # The alternateNames property
    alternate_names: Optional[List[str]] = None
    # The commonName property
    common_name: Optional[str] = None
    # The email property
    email: Optional[str] = None
    # The givenName property
    given_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizationName property
    organization_name: Optional[str] = None
    # The organizationUnitName property
    organization_unit_name: Optional[str] = None
    # The serialNumber property
    serial_number: Optional[str] = None
    # The surname property
    surname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SslCertificateEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SslCertificateEntity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SslCertificateEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..physical_address import PhysicalAddress

        from ..physical_address import PhysicalAddress

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "alternateNames": lambda n : setattr(self, 'alternate_names', n.get_collection_of_primitive_values(str)),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "givenName": lambda n : setattr(self, 'given_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "organizationUnitName": lambda n : setattr(self, 'organization_unit_name', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "surname": lambda n : setattr(self, 'surname', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("address", self.address)
        writer.write_collection_of_primitive_values("alternateNames", self.alternate_names)
        writer.write_str_value("commonName", self.common_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("givenName", self.given_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_str_value("organizationUnitName", self.organization_unit_name)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("surname", self.surname)
        writer.write_additional_data_value(self.additional_data)
    


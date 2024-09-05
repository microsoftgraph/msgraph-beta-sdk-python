from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .physical_address import PhysicalAddress

@dataclass
class CompanyDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Address of the company.
    address: Optional[PhysicalAddress] = None
    # Legal entity number of the company or its subdivision. For information on how to set the value for the companyCode, see profileSourceAnnotation.
    company_code: Optional[str] = None
    # Department Name within a company.
    department: Optional[str] = None
    # Company name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Office Location of the person referred to.
    office_location: Optional[str] = None
    # Pronunciation guide for the company name.
    pronunciation: Optional[str] = None
    # Secondary Department Name within a company.
    secondary_department: Optional[str] = None
    # Link to the company home page.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .physical_address import PhysicalAddress

        from .physical_address import PhysicalAddress

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "companyCode": lambda n : setattr(self, 'company_code', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "officeLocation": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "pronunciation": lambda n : setattr(self, 'pronunciation', n.get_str_value()),
            "secondaryDepartment": lambda n : setattr(self, 'secondary_department', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("address", self.address)
        writer.write_str_value("companyCode", self.company_code)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("pronunciation", self.pronunciation)
        writer.write_str_value("secondaryDepartment", self.secondary_department)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    


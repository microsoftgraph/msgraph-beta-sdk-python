from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

allowed_audiences = lazy_import('msgraph.generated.models.allowed_audiences')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
inference_data = lazy_import('msgraph.generated.models.inference_data')
person_data_sources = lazy_import('msgraph.generated.models.person_data_sources')

class ItemFacet(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def allowed_audiences(self,) -> Optional[allowed_audiences.AllowedAudiences]:
        """
        Gets the allowedAudiences property value. The audiences that are able to see the values contained within the associated entity. Possible values are: me, family, contacts, groupMembers, organization, federatedOrganizations, everyone, unknownFutureValue.
        Returns: Optional[allowed_audiences.AllowedAudiences]
        """
        return self._allowed_audiences
    
    @allowed_audiences.setter
    def allowed_audiences(self,value: Optional[allowed_audiences.AllowedAudiences] = None) -> None:
        """
        Sets the allowedAudiences property value. The audiences that are able to see the values contained within the associated entity. Possible values are: me, family, contacts, groupMembers, organization, federatedOrganizations, everyone, unknownFutureValue.
        Args:
            value: Value to set for the allowedAudiences property.
        """
        self._allowed_audiences = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemFacet and sets the default values.
        """
        super().__init__()
        # The audiences that are able to see the values contained within the associated entity. Possible values are: me, family, contacts, groupMembers, organization, federatedOrganizations, everyone, unknownFutureValue.
        self._allowed_audiences: Optional[allowed_audiences.AllowedAudiences] = None
        # The createdBy property
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Provides the dateTimeOffset for when the entity was created.
        self._created_date_time: Optional[datetime] = None
        # Contains inference detail if the entity is inferred by the creating or modifying application.
        self._inference: Optional[inference_data.InferenceData] = None
        # The isSearchable property
        self._is_searchable: Optional[bool] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # Provides the dateTimeOffset for when the entity was created.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Where the values within an entity originated if synced from another service.
        self._source: Optional[person_data_sources.PersonDataSources] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Provides the dateTimeOffset for when the entity was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Provides the dateTimeOffset for when the entity was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemFacet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemFacet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemFacet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_audiences": lambda n : setattr(self, 'allowed_audiences', n.get_enum_value(allowed_audiences.AllowedAudiences)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "inference": lambda n : setattr(self, 'inference', n.get_object_value(inference_data.InferenceData)),
            "is_searchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(person_data_sources.PersonDataSources)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inference(self,) -> Optional[inference_data.InferenceData]:
        """
        Gets the inference property value. Contains inference detail if the entity is inferred by the creating or modifying application.
        Returns: Optional[inference_data.InferenceData]
        """
        return self._inference
    
    @inference.setter
    def inference(self,value: Optional[inference_data.InferenceData] = None) -> None:
        """
        Sets the inference property value. Contains inference detail if the entity is inferred by the creating or modifying application.
        Args:
            value: Value to set for the inference property.
        """
        self._inference = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. The isSearchable property
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. The isSearchable property
        Args:
            value: Value to set for the isSearchable property.
        """
        self._is_searchable = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Provides the dateTimeOffset for when the entity was created.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Provides the dateTimeOffset for when the entity was created.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedAudiences", self.allowed_audiences)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("inference", self.inference)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("source", self.source)
    
    @property
    def source(self,) -> Optional[person_data_sources.PersonDataSources]:
        """
        Gets the source property value. Where the values within an entity originated if synced from another service.
        Returns: Optional[person_data_sources.PersonDataSources]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[person_data_sources.PersonDataSources] = None) -> None:
        """
        Sets the source property value. Where the values within an entity originated if synced from another service.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    

